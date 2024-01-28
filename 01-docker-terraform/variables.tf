variable "credentials" {
  description = "My Credentials"
  default     = "/home/gajop/.config/gcloud/tf-key.json"
  #ex: if you have a directory where this file is called keys with your service account json file
  #saved there as my-creds.json you could use default = "./keys/my-creds.json"
}


variable "project" {
  description = "Project"
  default     = "dtc-de-course-2024-412615"
}

variable "region" {
  description = "Region"
  #Update the below to your desired region
  default     = "asia-northeast-1"
}

variable "location" {
  description = "Project Location"
  #Update the below to your desired location
  default     = "asia-northeast1"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  #Update the below to what you want your dataset to be called
  default     = "gajop_dtc_de_course_2024_dataset"
}

variable "gcs_bucket_name" {
  description = "DTC DE Course 2024"
  #Update the below to a unique bucket name
  default     = "gajop_dtc_de_course_2024_bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}