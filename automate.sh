export GOOGLE_APPLICATION_CREDENTIALS=/home/ashik/nlp/authkey.json
curl https://en.wikipedia.org/wiki/Main_Page >wikipedia.html 2>null
sed -n "/In the news/,/Current_events/p" wikipedia.html >news.html
html2text news.html >news.txt
sed -i 's/_/ /g' news.txt
tail -n +2 news.txt >temp.txt ; mv temp.txt news.txt
head -n -1 news.txt >temp.txt ; mv temp.txt news.txt
python /home/ashik/nlp/first.py news.txt 1>indscore.txt
python /home/ashik/nlp/third.py news.txt 1>result.txt
echo "based on data from ">curtime.txt
date >>curtime.txt
cat result.txt /home/ashik/nlp/intro.txt curtime.txt news.txt indscore.txt totalscore.txt >output.txt
gsutil cp output.txt gs://nlpbucket/output-"`date`".txt
gsutil cp output.txt gs://nlpbucket/output.txt
gsutil cp result.txt gs://nlpbucket/result.txt
gsutil acl ch -u AllUsers:R gs://nlpbucket/output.txt
gsutil acl ch -u AllUsers:R gs://nlpbucket/result.txt
