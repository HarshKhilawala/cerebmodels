# ../executiveTest.py
import unittest
import os
import shutil
import importlib

from executive import ExecutiveControl

class ExecutiveControlTest(unittest.TestCase):

    def setUp(self):
        self.ec = ExecutiveControl() #instance for non: static & class methods.
        self.pwd = os.getcwd()

    def test_1_list_modelscales(self):
        x = len(self.ec.list_modelscales()) != 0
        self.assertEqual(x, True)

    def test_2_list_models(self):
        dummyscale_path = self.pwd+os.sep+"models"+os.sep+"dummyscale"
        for i in range(3): # create three dummymodels
            os.makedirs(dummyscale_path+os.sep+"dummymodel"+str(i+1))
        self.assertEqual(
            len(self.ec.list_models(modelscale="dummyscale")),
            3)
        shutil.rmtree(dummyscale_path)

    def test_3_choose_model(self):
        # NOTE: this only works if the 'minimal' script
        # ~/models/cells/model2015Masoli.py exists
        # 'minimal' => a class with __init__ method with
        # self.modelname = "PC2015Masoli.py"
        x = self.ec.choose_model( modelscale="cells",
                                  modelname="DummyTest" )
        self.assertEqual( x.modelname, "DummyTest" )

    def test_4_launch_model_NEURON_with_capability(self):
        pickedmodel = self.ec.choose_model( modelscale="cells",
                                            modelname="DummyTest" )
        parameters = {"dt": 0.01, "celsius": 30, "tstop": 100, "v_init": 65}
        self.assertEqual( self.ec.launch_model (
                              parameters = parameters,
                              onmodel = pickedmodel,
                              capabilities = {'model': 'produce_spike_train',
                                              'test': None} ),
                         "model was successfully simulated")

    def test_5_launch_model_NEURON_raw(self):
        pickedmodel = self.ec.choose_model( modelscale="cells",
                                            modelname="DummyTest" )
        parameters = {"dt": 0.01, "celsius": 30, "tstop": 100, "v_init": 65}
        self.assertEqual( self.ec.launch_model (
                              parameters = parameters,
                              onmodel = pickedmodel),
                         "model was successfully simulated")

if __name__ == '__main__':
    unittest.main()
