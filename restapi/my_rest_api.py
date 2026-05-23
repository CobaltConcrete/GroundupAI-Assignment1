from fastapi import FastAPI, UploadFile, File
import pandas as pd
import uvicorn
import chardet
from io import StringIO
from scipy.stats import kurtosis

app = FastAPI()

@app.post("/generateReport")
async def generate_report(file: UploadFile = File(...)):

    # Read file
    contents = await file.read()
    result = chardet.detect(contents)

    # Extract encoding
    encoding = result['encoding']

    # Convert to dataframe
    df = pd.read_csv(StringIO(contents.decode(encoding)))
    numerical_df = df.select_dtypes(include=['number'])

    # Init report
    report = {}

    # Read through & calc numerical cols
    for column in numerical_df.columns:
        report[column] = {
            "min": float(numerical_df[column].min()),
            "max": float(numerical_df[column].max()),
            "mean": float(numerical_df[column].mean()),
            "std": float(numerical_df[column].std()),
            "kurtosis": float(kurtosis(numerical_df[column], nan_policy="omit"))
        }

    return report

if __name__ == "__main__":
    uvicorn.run("my_rest_api:app", host="0.0.0.0", port=10000, reload=True)


