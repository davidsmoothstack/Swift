terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.2.0"

    }
  }

  backend "local" {}


  required_version = ">= 0.14.9"
}
