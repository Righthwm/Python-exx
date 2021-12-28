#!/bin/bash

gsutil mb -c regional -l us-central1 gs://vladvoica-b1
curl -L https://www.collinsdictionary.com/images/full/bucket_211822708_1000.jpg | gsutil cp - gs://vladvoica-b1/bucket.jpg

