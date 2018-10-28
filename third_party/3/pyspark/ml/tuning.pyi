# Stubs for pyspark.ml.tuning (Python 3.5)
#

from typing import overload
from typing import Any, Dict, List, Optional, Tuple, Type
from pyspark.ml import Estimator, Model
from pyspark.ml.evaluation import Evaluator
from pyspark.ml.param import Param
from pyspark.ml.param.shared import *
from pyspark.ml.util import *

ParamMap = Dict[Param, Any]

class ParamGridBuilder:
    def __init__(self) -> None: ...
    def addGrid(self, param: Param, values: List[Any]) -> 'ParamGridBuilder': ...
    @overload
    def baseOn(self, __args: ParamMap) -> ParamGridBuilder: ...
    @overload
    def baseOn(self, *args: Tuple[Param, Any]) -> ParamGridBuilder: ...
    def build(self) -> List[ParamMap]: ...

class ValidatorParams(HasSeed):
    estimator = ...  # type: Param
    estimatorParamMaps = ...  # type: Param
    evaluator = ...  # type: Param
    def setEstimator(self, value: Estimator) -> ValidatorParams: ...
    def getEstimator(self) -> Estimator: ...
    def setEstimatorParamMaps(self, value: List[ParamMap]) -> ValidatorParams: ...
    def getEstimatorParamMaps(self) -> List[ParamMap]: ...
    def setEvaluator(self, value: Evaluator) -> ValidatorParams: ...
    def getEvaluator(self) -> Evaluator: ...

class CrossValidator(Estimator, ValidatorParams, HasParallelism, MLReadable, MLWritable):
    numFolds = ...  # type: Param
    def __init__(self, estimator: Optional[Estimator] = ..., estimatorParamMaps: Optional[List[ParamMap]] = ..., evaluator: Optional[Evaluator] = ..., numFolds: int = ..., seed: Optional[int] = ..., parallelism: int = ...) -> None: ...
    def setParams(self, estimator: Optional[Estimator] = ..., estimatorParamMaps: Optional[List[ParamMap]] = ..., evaluator: Optional[Evaluator] = ..., numFolds: int = ..., seed: Optional[int] = ..., parallelism: int = ...) -> CrossValidator: ...
    def setNumFolds(self, value: int) -> CrossValidator: ...
    def getNumFolds(self) -> int: ...
    def copy(self, extra: Optional[ParamMap] = ...) -> CrossValidator: ...
    def write(self) -> MLWriter: ...
    @classmethod
    def read(cls: Type[CrossValidator]) -> MLReader: ...

class CrossValidatorModel(Model, ValidatorParams, MLReadable, MLWritable):
    bestModel = ...  # type: Model
    avgMetrics = ...  # type: List[float]
    def __init__(self, bestModel: Model, avgMetrics: List[float] = ...) -> None: ...
    def copy(self, extra: Optional[ParamMap] = ...) -> CrossValidatorModel: ...
    def write(self) -> MLWriter: ...
    @classmethod
    def read(cls: Type[CrossValidatorModel]) -> MLReader: ...

class TrainValidationSplit(Estimator, ValidatorParams):
    trainRatio = ...  # type: Param
    def __init__(self, estimator: Optional[Estimator] = ..., estimatorParamMaps: Optional[List[ParamMap]] = ..., evaluator: Optional[Evaluator] = ..., trainRatio: float = ..., seed: Optional[int] = ...) -> None: ...
    def setParams(self, estimator: Optional[Estimator] = ..., estimatorParamMaps: Optional[List[ParamMap]] = ..., evaluator: Optional[Evaluator] = ..., trainRatio: float = ..., seed: Optional[int] = ...) -> TrainValidationSplit: ...
    def setTrainRatio(self, value: float) -> TrainValidationSplit: ...
    def getTrainRatio(self) -> float: ...
    def copy(self, extra: Optional[ParamMap] = ...) -> TrainValidationSplit: ...

class TrainValidationSplitModel(Model, ValidatorParams):
    bestModel = ...  # type: Model
    validationMetrics = ...  # type: List[float]
    def __init__(self, bestModel: Model, validationMetrics: List[float] = ...) -> None: ...
    def copy(self, extra: Optional[ParamMap] = ...) -> TrainValidationSplitModel: ...
