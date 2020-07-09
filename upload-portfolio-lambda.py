import boto3
import io
import zipfile

s3 = boto3.resource('s3')

portfolio_bucket = s3.Bucket('portfolio.kmoberg.cloud')
build_bucket = s3.Bucket('portfoliobuild.kmoberg.cloud')

portfolio_zip = io.BytesIO()
build_bucket.download_fileobj('portfoliobuild.zip', portfolio_zip)

with zipfile.ZipFile(portfolio_zip) as myzip:
    for nm in myzip.namelist():
        obj = myzip.open(nm)
        portfolio_bucket.upload_fileobj(obj, nm)
        portfolio_bucket.Object(nm).Acl().put(ACL='public-read')