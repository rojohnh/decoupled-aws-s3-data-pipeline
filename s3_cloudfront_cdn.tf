# Headless Infrastructure Definition
resource "aws_s3_bucket" "data_lake" {
  bucket = "dite-headless-assets"
}

resource "aws_cloudfront_distribution" "cdn" {
  origin {
    domain_name              = aws_s3_bucket.data_lake.bucket_regional_domain_name
    origin_id                = "S3-dite-headless-assets"
    origin_access_control_id = aws_cloudfront_origin_access_control.oac.id
  }

  enabled             = true
  default_root_object = "manifest.json"

  default_cache_behavior {
    allowed_methods  = ["GET", "HEAD"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = "S3-dite-headless-assets"
    viewer_protocol_policy = "redirect-to-https"
  }
}
