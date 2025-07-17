import azure.functions as func
import logging
import requests

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="trigger-databricks")
def trigger_databricks(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('🚀 Triggering Databricks job from Azure Function')

    # ✅ Replace with your values
    databricks_instance = "https://adb-496094116969414.14.azuredatabricks.net"
    job_id = "785878784148634"
    token = "dapi130c92fd159278e4c30c885f189ba616"

    api_url = f"{databricks_instance}/api/2.1/jobs/run-now"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "job_id": job_id
    }

    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code == 200:
        return func.HttpResponse("✅ Databricks job triggered successfully!", status_code=200)
    else:
        return func.HttpResponse(f"❌ Failed: {response.text}", status_code=500)
