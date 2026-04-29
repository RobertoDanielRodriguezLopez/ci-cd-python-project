resource "local_file" "environment_definition" {
  filename = "${path.module}/${var.environment}.txt"

  content = <<EOF
Application: ${var.app_name}
Environment: ${var.environment}
Owner: ${var.owner}
EOF
}
