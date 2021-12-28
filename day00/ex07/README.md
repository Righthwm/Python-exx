HEAD request este foarte similară cu GET request, cu excepția faptului că serverul returnează doar anteturi HTTP fără un corp de răspuns. 
Pentru a face un HEAD request cu Curl, trebuie să utilizam -I. 
Parametrul liniei de comandă -I îi spune lui Curl să trimită o cerere HTTP HEAD pentru a primi doar anteturi HTTP.
X-Powered-By este un antet de răspuns HTTP non-standard comun (majoritatea antetelor prefixate cu „X-” sunt nestandard). 
Este adesea inclus în mod implicit în răspunsurile construite printr-o anumită tehnologie de scriptare. 