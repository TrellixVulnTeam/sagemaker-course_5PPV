# Exercise 1

- Create a new S3 bucket for your "team". It should start with `sagemaker-data`
- Upload the dataset `boston_dataset.csv` from this repo
- Create a Notebook instance. It should be of type `ml.t2.medium` and create a Role for it. Please set the Tags attribute as follows:
```
Tag: Course
Value: Intro-sagemaker
```

- Set the kernel to `conda_tensorflow_p36` and Print `Hello world`
- Stop the Notebook Instance!