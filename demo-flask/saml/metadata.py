from onelogin.saml2.idp_metadata_parser import OneLogin_Saml2_IdPMetadataParser

idp_data = OneLogin_Saml2_IdPMetadataParser.parse_remote('https://metadata.test.surfconext.nl/idp-metadata.xml')
