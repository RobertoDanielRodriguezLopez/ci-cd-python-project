data "aws_security_group" "app_sg" {
  name   = "ci-cd-python-sg"
  vpc_id = var.vpc_id
}
