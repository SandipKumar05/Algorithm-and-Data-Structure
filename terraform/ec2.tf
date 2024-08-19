# Specify the required Terraform version
terraform {
  required_version = ">= 1.0.0"

  backend "s3" {
    bucket = "sandip-test"
    key = "terraform.tfstate"
    region = "us-east-1"
  }

  # Specify the required provider versions
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

# Configure the AWS provider
provider "aws" {
  region = "us-west-2"  # Replace with your preferred region
}

# Define a security group that allows SSH access
resource "aws_security_group" "example" {
  name_prefix = "example-"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Define the EC2 instance
resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"  # Replace with a valid AMI ID for your region
  instance_type = "t2.micro"

  # Use the security group created above
  vpc_security_group_ids = [aws_security_group.example.id]

  # Use an existing key pair
  key_name = "my-key-pair"  # Replace with your key pair name

  # Add tags to the instance
  tags = {
    Name = "example-instance"
  }
}
