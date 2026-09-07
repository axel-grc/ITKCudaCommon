import itk


def test_set_default_cuda_device_api():
    # Available at top-level itk.
    assert hasattr(itk, "set_default_cuda_device")

    # Setting to an integer device index should be reflected by the getter.
    itk.set_default_cuda_device(0)
    assert itk.CudaDataManager.get_default_device() == 0

    # Setting to -1 resets to automatic selection.
    itk.set_default_cuda_device(-1)
    assert itk.CudaDataManager.get_default_device() == -1
