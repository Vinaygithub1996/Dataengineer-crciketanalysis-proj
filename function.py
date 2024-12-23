from googleapiclient.discovery import build # type: ignore


def trigger_df_job(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    project = "storied-shell-442103-t8"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "bq-load",  # Provide a unique name for the job
        "parameters": {
        "inputFilePattern": "gs://bckt-landing-zone1/user.csv",
        "JSONPath": "gs://bckt-df-metadata/bq.json",
        "outputTable": "storied-shell-442103-t8:user_data.users",
        "bigQueryLoadingTemporaryDirectory": "gs://bckt-df-metadata",
        "javascriptTextTransformGcsPath": "gs://bckt-df-metadata/udf.js",
        "javascriptTextTransformFunctionName": "transform"
    }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response) 