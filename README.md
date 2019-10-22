# caffe2mlmodel
Caffe model (.caffemodel) convert to CoreML model (.model) example code.

Open anaconda terminal to create a new virtual environment

```
conda create --name caffe
```

Then, activate the virtual environment

```
conda activate caffe
```

Install **Python** (ex: version 3.6.9)

```
conda install python=3.6.9
```

Install **CoreML Tools** (ex: version 3.0)
```
pip install -U coremltools==3.0
```

You can check your all installation successful or not.

```
$ python

>> import coremltools
>> 
```

It is successful if you **import coremltools** but do not get the error message.
