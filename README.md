This is a application demo of CycleGAN, filling colors automatically based on black-and-white line drafts of a fixed size of 256x256.

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

And here are some training results during the training period.

Original sketch:
![origin](/images/origin.jpg)

Results during the training:
![5_100](/images/5_100.png) ![14_0](/images/14_0.png)  ![23_0](/images/23_0.png) ![44_100](/images/44_100.png) ![333_100](/images/333_100.png) ![341_0](/images/341_0.png) ![342_0](/images/342_0.png) ![347_0](/images/347_0.png) ![348_0](/images/348_0.png) ![353_0](/images/353_0.png)