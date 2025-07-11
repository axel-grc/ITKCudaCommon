#-----------------------------------------------------------------------------
# Find ITK to include ITK_USE_FILE and correctly configure dynamic libraries.
if (NOT ITK_DIR)
  set(ITK_DIR ${ITK_BINARY_DIR}/CMakeTmp)
endif()
find_package(ITK REQUIRED COMPONENTS ${ITK_MODULE_CudaCommon_DEPENDS})
include(${ITK_USE_FILE})

itk_module_test()

set(CudaCommonTests
 itkCudaSquareImageFilterTest.cxx
  )

CreateTestDriver(CudaCommon "${CudaCommon-Test_LIBRARIES}" "${CudaCommonTests}")

itk_add_test(NAME itkCudaSquareImageFilterTest
  COMMAND CudaCommonTestDriver
  itkCudaSquareImageFilterTest
  )

# -----------------------------------------------------------------------------
# cudacommon_python_test(testname script [ARGS...])
function(cudacommon_python_test testname script)
  if(NOT Python3_EXECUTABLE)
    find_package(Python3 COMPONENTS Interpreter REQUIRED)
  endif()

  # Create the test: run "python script [ARGS...]"
  add_test(NAME ${testname}
    COMMAND ${Python3_EXECUTABLE} ${script} ${ARGN}
  )

  set_tests_properties(${testname}
    PROPERTIES
      LABELS        "Python"
      WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
  )
endfunction()

# -----------------------------------------------------------------------------
if(CudaCommon_PYTHON_TESTS)
    cudacommon_python_test(itkCudaImageFromImagePythonTest itkCudaImageFromImageTest.py)
endif()