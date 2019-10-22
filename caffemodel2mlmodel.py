import coremltools

# Load caffemodel, prototxt and class_labels for convert function
coreml_model = coremltools.converters.caffe.convert(('LR/without_fc6-7/location_recog_iter_20000.caffemodel',
                                                     'LR/without_fc6-7/vgg_location_deploy.prototxt'),
                                                    class_labels='LR/class_labels.txt',
                                                    image_input_names='data',
                                                    is_bgr=True)
# Save mlmodel
coreml_model.save('LR_without_fc6_7.mlmodel')
