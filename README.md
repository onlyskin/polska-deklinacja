AWS lambda function to practise declining Polish nouns and number words. Exposed via HTTP endpoint.

Uses `pytest` for testing and the serverless framework to manage AWS deployment.
Serverless dependencies can be installed from the `package.json` using `node` and
the python requirements can be installed from the `requirements.txt`.

Deployment with `sls deploy` requires an account with AWS credentials to be set up.
