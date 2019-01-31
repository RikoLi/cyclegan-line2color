This is a funny demo for CycleGAN, filling colors automatically based on black-and-white line drafts of a fixed size of 256x256.

## Usage
### Environment
To run the code, an environment of TensorFlow and Keras is needed.

### Dataset
To train the model, you have to prepare 4 datasets:
* trainA: Line drafts for training.
* trainB: Colored avaters for training.
* testA: Line drafts for testing.
* testB: Colored avaters for testing.

To start training, open cmd and input:
`python main.py -t`

Training options can be modified in main.py.

## References
Codes are edited from gan-zoo on GitHub.

## Result
First row: line draft to colored image
Second row: colored image to line draft
![190_0](/images/190_0.png)