variable "aws_region" { type = string; default = "us-east-1" }
variable "environment" { type = string }
variable "container_image" { type = string; default = "placeholder" }

variable "sagemaker_endpoint_name_param" {
  type        = string
  description = "The name of the SSM parameter for the SageMaker endpoint name."
  default     = "ssp/ai/recommender_endpoint_name"
}
