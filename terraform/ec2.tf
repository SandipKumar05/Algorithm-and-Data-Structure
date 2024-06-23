# My Module

# This module creates an AWS EC2 instance.

## Usage

module "example" {
  source        = "./my-module"
  ami_id        = "ami-12345678"
  instance_type = "t2.micro"
  instance_name = "example-instance"
}

resources