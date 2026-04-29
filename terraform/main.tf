module "app_environment" {
  source = "./modules/app_environment"

  environment = var.environment
  app_name    = var.app_name
  owner       = var.owner
}
