# Workshop 2

In this workshop we will create a SageMaker Pipeline that will train and evaluate a tensorflow model to predict house value.
Read all these instructions before starting. To look for a place to start check this: https://docs.aws.amazon.com/sagemaker/latest/dg/define-pipeline.html

The solutions are in the solutions folder, but try to do it yourself :) You have the rest of the day! 
Also, if you want, run the solutions and then expand over it or ask me away! I haven't prepared it but we can work on it together!!

- The pipeline should:

    - Preprocess the housing data
    - Train the tensorflow model
    - Evalute it
    - Check if the MSE is lower than a parameter threshold
    - If it is then register and create the model
  
The parameters should be:

    - the input_data S3 location
    - The preprocessing instance type
    - The training_instance_type
    - The number of epochs to train
    - The threshold  for the MSE

- The preprocessing should only apply the standard scaler from sklearn as we have done in a previous lab
- The model to train is:

```
    inputs = tf.keras.Input(shape=(8,))
    hidden_1 = tf.keras.layers.Dense(8, activation='tanh')(inputs)
    hidden_2 = tf.keras.layers.Dense(4, activation='sigmoid')(hidden_1)
    outputs = tf.keras.layers.Dense(1)(hidden_2)
    return tf.keras.Model(inputs=inputs, outputs=outputs)
```

If you feel stuck, just create the pipeline which is more straightforward and take as given the preprocess, train, and evaluate scripts!

Test executions with a super low threshold to see that some steps won't run! If we had setup email, we could create a lambda for email notifications and a Lambda step for that, being triggered in that case!


