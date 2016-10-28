#include <stdio.h>
#include <iostream>
#include <string.h>
#include "harmony10.h"
#include "harmony_efim.h"
#include "testlib.h"
#include "libxml/xmlreader.h"
#ifdef HAVE_CONFIG_H
#include <config.h>
#endif

using namespace std;

FILE *fp;
HarmonyServerHandle *Serhandle;

char *trim_space( char *str )
{
	char *end;

	while( isspace( *str ) || *str == '\t' ) str++;

	if( *str == 0 )
		return str;

	end = str + strlen( str ) - 1;
	while( end > str && ( isspace( *end ) || *end == '\t' ) ) end--;

	*( end + 1 ) = 0;

	return str;
}

int get_value ( const char *key, char **value )
{
	char *local_value;
	int local_ret;
	HarmonyResult ret;

	ret = HARMONY_RESULT_OK;
	HarmonySessionHandle local_ses_handle;

	local_ret = 0;

	fprintf ( fp, "------------------------------------\n" );
	fprintf ( fp, "Entered in function get_value\n" );
	fprintf ( fp, "------------------------------------\n" );
	ret = ATTR_openSession ( Serhandle, &local_ses_handle, NULL );
	if ( ret ) {
		fprintf ( fp, "Failed to open session for ATTR_openSession: error code %d\n", ret );
		fprintf ( fp, "------------------------------------\n" );
		fprintf ( fp, "Exited from function get_value\n" );
		fprintf ( fp, "------------------------------------\n" );
		return -1;
	}

	ret = ATTR_getDefault ( &local_ses_handle, 0, key, &local_value, NULL );
	if ( ret ) {
		if ( ret == HARMONY_RESULT_KEY_NOT_FOUND ) {
			ret = EFIM_dictRead ( Serhandle, "XJ7_SYSTEM", key, &local_value, NULL );
			if ( ret != HARMONY_RESULT_OK ){
				fprintf ( fp, "Failed to open session for EFIM_dictRead : error code %d\n", ret );
				local_ret = -1;
				goto clean_exit;
			}
		}
		if ( ret ) {
			fprintf ( fp, "Failed to open session for ATTR_getDefault for key \"%s\": error code %d\n", key, ret );
			local_ret = -1;
			goto clean_exit;
		}
	}

	fprintf ( fp, "%s = %s\n", key, local_value );

	*value = local_value;

clean_exit:
	ret = ATTR_closeSession ( &local_ses_handle, NULL );
	if ( ret ) {
		fprintf ( fp, "Failed to open session for ATTR_closeSession : error code %d\n", ret );
		return -1;
	}

	fprintf ( fp, "------------------------------------\n" );
	fprintf ( fp, "Exited from function get_value\n" );
	fprintf ( fp, "------------------------------------\n" );

	return local_ret;
}

char *processNode(xmlTextReaderPtr reader ) {
	const xmlChar *name, *value;
	char *val;

	val = NULL;

	name = xmlTextReaderConstName(reader);
	if (name == NULL)
		name = BAD_CAST "--";

	value = xmlTextReaderConstValue(reader);
	if (value != NULL) {
		val = trim_space ( ( char * ) value );
		if ( strlen ( val ) > 2 )
			printf ( "value = %s\n", val );
		else
			val = NULL;
	}

	return val;
}


int streamFile(const char *filename, const xmlChar *pattern, char ***presets, int *array_length ) {
	xmlTextReaderPtr reader, doc_ptr;
	xmlDocPtr doc;
	char **local_presets;
	char *value;
	int array_len;
	array_len = 0;


	fprintf ( stdout, "Entered function free parser\n" ); 
	local_presets = ( char ** ) calloc ( 1, 6 * sizeof ( char * ) );

	reader = xmlReaderForFile(filename, NULL, 0);
	if (reader != NULL) {
		int ret;
		if (xmlTextReaderPreservePattern(reader, pattern, NULL) < 0) {
			fprintf(stderr, "%s : failed add preserve pattern %s\n",
					filename, (const char *) pattern);
		}

		ret = xmlTextReaderRead(reader);
		while (ret == 1) {
			ret = xmlTextReaderRead(reader);
		}
		if (ret != 0) {
			fprintf(stderr, "%s : failed to parse\n", filename);
			xmlFreeTextReader(reader);
		}

		doc = xmlTextReaderCurrentDoc(reader);
		if ( doc != NULL ) {	
			doc_ptr = xmlReaderWalker ( doc );
			if ( doc_ptr != NULL ) {
				ret = xmlTextReaderRead ( doc_ptr );
				while ( ret == 1 ) {	
					value = processNode( doc_ptr );	
					if ( value != NULL ) {
						fprintf ( stdout, "value = %s\n", value );
						local_presets[array_len] = ( char * ) calloc ( 1, 128 ); 
						strcpy ( local_presets[array_len], value );	
						fprintf ( stdout, "ramesh = %s\n", local_presets[array_len] );
						array_len++;
					}
					ret = xmlTextReaderRead ( doc_ptr );
					fprintf ( stdout, "ret value of ret = %d\n", ret );
				}
			}
			else {
				xmlFreeTextReader(doc_ptr);
				xmlFreeTextReader(reader);
				return -1;
			}

		}
		else {

			xmlFreeTextReader(reader);
			return -1;
		}
	} else {
		fprintf(stderr, "Unable to open %s\n", filename);
		return -1;
	}
	*array_length = array_len;
	*presets = local_presets;	
	fprintf ( stdout, "exited function free parser\n" ); 

	return 0;
}

int resman ( char ***names, int *num_names ) { 
	HarmonyAttributes **settings;
	HarmonySessionHandle Seshandle;
	HarmonyResult res;
	int local_num_names;
	char **local_names;
	int status_flag;

	status_flag = local_num_names = 0;

	res = RESMAN_openSession(Serhandle, &Seshandle, NULL);
	if(res)
	{
		fprintf( fp, "RESMAN_openSession returned error is %d\n", res);
		status_flag = 1;
	}
	else {
		fprintf( fp, "RESMAN_openSession is successfull\n");
		fprintf( stdout, "RESMAN_openSession is successfull\n");

		res = RESMAN_getResourceWithSettingsInContainer(&Seshandle, "preset", &local_names, &settings, &local_num_names, NULL);
		if(res)
		{
			fprintf( fp, "RESMAN_getResource returned error is %d\n", res);
			status_flag = 1;
		}

		res = RESMAN_closeSession(&Seshandle, NULL);
		if(res)
		{
			fprintf( fp, "RESMAN_closeSession returned error is %d\n", res);
			fprintf( stdout, "RESMAN_closeSession returned error is %d\n", res);
			status_flag = 1;
		}
		else {
			fprintf( fp, "RESMAN_closeSession is successfull\n");
			fprintf( stdout, "RESMAN_closeSession is successfull\n");
		}
	}

	*names = local_names;
	*num_names = local_num_names;

	return status_flag;
}

int main(int argc,char *argv[])
{
	char *hostname = NULL, **names, *preset_version;
	HarmonyResult res=HARMONY_RESULT_OK;
	int status_flag;
	char *log_file;
	int num_names;

	//const char *presets_names_inches[] = { "Half_Letter_Booklet", "Letter_Booklet", "Letter_Duplex_Staple","Letter_Duplex_Grayscale", "Letter_2up_Tabloid" };	
	//const char *presets_names_metric[] = { "A4_2up_A3", "A4_Booklet", "A4_Duplex_Grayscale","A4_Duplex_Staple", "A5_Booklet" };	
	//const char *intent_preset_names[] = { "Small_booklet", "Large_booklet", "Duplex_staple","Duplex_grayscale", "2up_landscape" };


	status_flag = 0;
	preset_version = NULL;

	TestLib::AutoTestConfig cfg(argc, argv);

		hostname = ( char * ) calloc ( 1, sizeof ( char ) * 128 );
	strcpy( (char* )hostname, (char *)cfg.target_ip.c_str() );    //Obtain IP Address of the Fiery Server 

	log_file = ( char * ) calloc ( 1, sizeof ( char ) * 256 );
	strcpy ( log_file, ( char * ) cfg.log_dir.c_str());
	strcat ( log_file, "/Built_In_Preset.txt" );
	fprintf ( stdout, "log_file = %s\n", log_file );

	fp = fopen ( log_file, "w" );
	if ( fp == NULL ) { 
		fprintf ( stderr, "Failed to open file Built_In_Preset.txt\n" );
		free ( log_file );
		free ( hostname );
		return -1;
	}
	free ( log_file );

	res = INIT_connect( hostname, "admin", "Fiery.1", 0, 0, "trpc", -1, -1, -1, 1, 0, &Serhandle, NULL );
	if( res )
	{
		fprintf( fp, "failed to connect to server %s and return value is %d", hostname, res );
		status_flag = 1;
	}
	else {
		fprintf( fp, "Connected to server=%s succesfully\n", hostname);
		fprintf( stdout, "Connected to server=%s succesfully\n", hostname);
		int ret;
		ret = 0;

		{
			const char *key = "EFISYSVER";
			char *value;

			ret = get_value ( key, &value );
			if ( ret ) { fprintf ( fp, "failed to do get value of key \"%s\"\n", key ); return -1; }

			if ( !strcmp ( value, "FS100 Pro" ) || !strcmp ( value, "FS100" ) || !strcmp ( value, "10" ) || !strcmp ( value, "9 Rel2" ) || !strcmp ( value, "9e Rel2" ) || !strcmp ( value, "9" ) || !strcmp ( value, "9e" ) || !strcmp ( value, "8" ) || !strcmp ( value, "8e" ) || !strcmp ( value, "8 Rel2" ) || !strcmp ( value, "8e Rel2" ) || !strcmp ( value, "8e Release 2" ) || !strcmp ( value, "8 Release 2" )) //To Check system is below/equal to flame4 
			{
				fprintf ( fp, "The Built-in presets is not applicable from Flame4 below\n" );
				fclose ( fp );
				return 44;
			}
		}

		ret = resman ( &names, &num_names ); 
		if ( !ret ) {
			char *os_locale;
			char *fiery_locale;
			char **presets_ptr;
			int array_len;

			presets_ptr = NULL;	
			array_len = ret = 0;

			HarmonyDateFormat date_format; 
			HarmonyNumberFormat number_format;
			HarmonyMeasurementUnit measurement_unit, default_paper_size;


			fprintf ( fp, "The Built in presets present in server are as follows\n" );
			fprintf ( stdout, "The Built in presets present in server are as follows\n" );
			fprintf ( stdout, "num_name = %d\n", num_names );
			fprintf ( fp, "-------------------------------\n" ); 
			for ( int i =0; i < num_names; i++ ){
				fprintf ( fp, "%s\n", names[i] ); 
				fprintf ( stdout, "%s\n", names[i] ); 
			}
			fprintf ( fp, "-------------------------------\n" ); 

			res = SERVER_getSystemLocale4 ( Serhandle, &fiery_locale, &os_locale, &date_format, &number_format, &measurement_unit, &default_paper_size, NULL );
			if ( !res ) {

				fprintf ( fp, "os_locale = %s\n", os_locale );
				fprintf ( stdout, "os_locale = %s\n", os_locale );
				fprintf ( stdout, "ramesh\n" );
				fprintf ( stdout, "default_paper_size= %d\n", default_paper_size );

				res = FEAT_getFeatureValue ( Serhandle, "DEFAULT_SERVER_PRESETS_VERSION", &preset_version, NULL );
				if ( res == HARMONY_RESULT_OK || res == HARMONY_RESULT_KEY_NOT_FOUND ) {
					int ver;
					ver = 0;

					if ( res == HARMONY_RESULT_OK ) 
						ver = atoi ( preset_version ); 
					char *parser = ( char * ) calloc ( 1, sizeof ( char ) * 256 );	

					if ( ver == 1 )  {
						strcpy ( parser, "presets/intent_presets/" );
						strcat ( parser, os_locale );
					}
					else if ( res == HARMONY_RESULT_KEY_NOT_FOUND ) {
					
						fprintf ( stdout, "preset_version = %d\n", preset_version );
						fprintf ( stdout, "default paper size = %d\n", default_paper_size );
						if ( default_paper_size == HARMONY_MEASUREMENT_UNIT_METRIC ){
							fprintf ( stdout, "ramesh metric\n" );
							strcpy ( parser, "presets/metric_presets/" );
							strcat ( parser, os_locale );
							fprintf ( stdout, "parser = %s\n", parser );
						}
						else if ( default_paper_size == HARMONY_MEASUREMENT_UNIT_US ) {
							strcpy ( parser, "presets/inches_presets/" );
							strcat ( parser, os_locale );
						}
					}
					else {
						fprintf ( fp, "Invalid default paper size\n" );
						fprintf ( stdout, "Invalid default paper size\n" );
						status_flag = 1;
					}
					fprintf ( stdout, "parser = %s\n", parser ); 

					ret = streamFile( "tests/Built_In_Preset/preset.xml", (const xmlChar *) parser, &presets_ptr, &array_len );
					free ( parser );
					fprintf ( stdout, "array length = %d\n", array_len );
					if ( array_len ) {
						fprintf ( fp, "The Built in presets parsed from xml file are as follows\n" );
						fprintf ( stdout, "The Built in presets parsed from xml file are as follows\n" );
						fprintf ( stdout, "array_len = %d\n", array_len );
						fprintf ( fp, "-------------------------------\n" ); 
						for ( int i =0; i < array_len; i++ ){
							fprintf ( fp, "%s\n", presets_ptr[i] ); 
							fprintf ( stdout, "%s\n", presets_ptr[i] ); 
						}	
						fprintf ( fp, "-------------------------------\n" ); 
						fprintf ( stdout, "-------------------------------\n" ); 


						fprintf ( stdout, "Compare the presets present in xml and in server\n" );
						fprintf ( fp, "Compare the presets present in xml and in server\n" );
						for ( int j = 0; j < 5; j++ ) {
							int flag;
							flag = 0;
							for ( int i = 0; i < num_names; i++ ) {
								if ( !strcmp ( presets_ptr[j], names[i] ) ) {
									flag = 1;
									fprintf ( fp, "%s\n", presets_ptr[j] );
									fprintf ( stdout, "%s\n", presets_ptr[j] );
									break;
								}
							}
							if ( !flag ){
								fprintf ( fp, "!!!Failed, The preset \"%s\" is not present in server\n", presets_ptr[j] );
								fprintf ( stdout, "!!!Failed, The preset \"%s\" is not present in server\n", presets_ptr[j] );
								status_flag = 1;	
							}
						}
						if ( status_flag == 1 )
							fprintf ( fp, "!!!Failed to compare the server presets with xml presets\n" );
						else
							fprintf ( fp, "!!!Successfully compared the server presets with xml presets\n" );

						fprintf ( stdout, "Freeing of presets_ptr is done successfully\n" );
					}
					else {
						fprintf ( fp, "Failed to parse the file preset.xml\n" );
						status_flag = 1;
					}
				}
				else {
					fprintf ( fp, "!!!Failed to perform FEAT_getFeatureValue, return code = %d\n", res );
					status_flag = 1;
				}
			}		
			else {
				fprintf ( fp, "Failed to perform SERVER_getSystemLocale4, return code \"%d\"\n", res );
				status_flag = 1;	
			}
		}
		else {
			fprintf ( fp, "!!!Failed to fetch the presets of server\n" ); 
			status_flag = 1;	

		}

		res = INIT_disconnect( Serhandle, NULL );
		if(res)
		{
			fprintf( fp, "Failed to disconnect forcefully from the server=\n");
			fprintf( stdout, "Failed to disconnect forcefully from the server=\n");
		}
		else {
			fprintf( fp, "server=%s Disconnected forcefully \n",hostname);
			fprintf( stdout, "server=%s Disconnected forcefully \n",hostname);
		}
	}

	free ( hostname );
	fclose ( fp );

	return status_flag;
}
