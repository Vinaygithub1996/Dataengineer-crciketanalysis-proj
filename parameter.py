"parameters": {
        "inputFilePattern": "gs://bckt-landing-zone1/user.csv",
        "JSONPath": "gs://bckt-df-metadata/bq.json",
        "outputTable": "storied-shell-442103-t8:user_data.users",
        "bigQueryLoadingTemporaryDirectory": "gs://bckt-df-metadata",
        "javascriptTextTransformGcsPath": "gs://bckt-df-metadata/udf.js",
        "javascriptTextTransformFunctionName": "myTransform" # type: ignore
    } # type: ignore