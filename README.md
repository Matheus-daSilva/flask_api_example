# flask_api_example

<h3>How to run the project after clone it?</h3>
<ul>
  <li>to build de image: docker build -t flask-smorest-api .</li>
  <li>to run the image: docker run -dp 5000:5000 -w /app -v "$(pwd):/app" flask-smorest-api sh -c "flask run"<li>
  <li>to run the containers: docker compose up -d</li>
  <li>to run the queue image: docker build -t rest-api-recording-email .</li>
  <li>to run the the image rest-api-recording-email on a container: docker run -p 3000:3000 rest-api-recording-email sh -c "flask run --host 0.0.
0.0"</li>
  <li>to run rq: docker run -w /app rest-api-recording-email sh -c "rq worker -u rediss://red-cpu95amehbks73a95peg:eW9koDQDRTJTGmN6uCKwCULWKPJ0t9QD@frankfurt-redis.render.com:6379 emails"</li>
</ul>
<p>Now you are able to make requests on 5000 port</p>
