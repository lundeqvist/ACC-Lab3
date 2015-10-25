# ACC-Lab3

1. source rc-file
2. python create-broker-instance
3. set master_ip in userdata-worker.yml to ip of broker
4. python create-worker-instances [n_workers_to_create]
5. wait until user data of broker finished loading
6. go to http://[ip_of_broker]:5000/pronouns2
