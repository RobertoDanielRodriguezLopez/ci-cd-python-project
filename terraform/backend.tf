terraform {
  backend "s3" {
    bucket         = "ci-cd-terraform-state-demo-robertodaniel"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}