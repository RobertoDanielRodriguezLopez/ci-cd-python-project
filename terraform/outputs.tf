output "ec2_public_ip" {
  description = "Public IP of the EC2 instance"
  value       = aws_instance.ci_cd_instance.public_ip
}

output "ssh_command" {
  description = "SSH command"
  value       = "ssh ubuntu@${aws_instance.ci_cd_instance.public_ip}"
}
