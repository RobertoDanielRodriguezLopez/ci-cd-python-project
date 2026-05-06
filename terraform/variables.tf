variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "instance_type" {
  description = "EC2 instance type (Free Tier)"
  type        = string
  default     = "t2.micro"
}

variable "key_name" {
  description = "SSH key pair name for the EC2 instance"
  type        = string
  default     = "ci-cd-python-key"
}
