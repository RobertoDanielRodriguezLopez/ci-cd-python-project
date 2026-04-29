variable "environment" {
  description = "Deployment environment (dev, qa, prod)"
  type        = string
}

variable "app_name" {
  description = "Application name"
  type        = string
}

variable "owner" {
  description = "Team or owner of the application"
  type        = string
}
