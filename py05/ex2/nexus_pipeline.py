#!/usr/bin/env python3

from typing import Any, List, Union, Protocol
from abc import ABC, abstractmethod


class ProcessingStage(Protocol):
    def process(data: Any) -> Any: ...


class InputStage:

    def process(self, data: Any) -> Any:
        print(f"InputStatge: Reading data {data}")
        if data is None:
            raise ValueError("No data provided to InputStage")

        if isinstance(data, dict):
            return data
        return {"data": data}


class TransformStage:

    def process(self, data: Any) -> Any:
        print("Transfroming data: Enriched with metadata")
        if isinstance(data, dict):
            return {
                k: v.upper() if isinstance(v, str) else v
                for k, v in data.items()
            }
        return data


class OutputStage:

    def process(self, data: Any) -> str:
        print("OutputStage: ", end="")
        if isinstance(data, dict):
            print(f"processe data: {data} ")
        return str(data)


class ProcessingPipeline(ABC):

    def __init__(self, pipeline_id: str) -> None:
        self.stages: List[ProcessingStage] = []
        self.pipeline_id = pipeline_id

    def add_stage(self, stage: "ProcessingStage") -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(data: Any) -> Union[Any, str]:
        pass


class JSONAdapter(ProcessingPipeline):

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        result = data
        print(f"\nJSONAdapter - {self.pipeline_id}] Starting processing...")
        for stage in self.stages:
            result = stage.process(result)
        print(f"[JSonAdapter - {self.pipeline_id}] Processing complete!\n")
        return result


class CSVAdapter(ProcessingPipeline):

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[Any, str]:

        print(f"\nCSVAdapter - {self.pipeline_id}] Starting processing...")
        result = data
        for stage in self.stages:
            result = stage.process(result)
        print(f"[CSVAdapter - {self.pipeline_id}] Processing complete!\n")
        return result


class StreamAdapter(ProcessingPipeline):

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[Any, str]:
        result = data
        print("\n[StreamAdapter - {self.pipeline_id}] Starting processing...")
        for stage in self.stages:
            result = stage.process(result)
        print(f"[StreamAdapter - {self.pipeline_id}] Processing complete!\n")
        return result


class NexusManager:

    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, new_pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(new_pipeline)
        print(
            f"Added pipeline: {new_pipeline.__class__.__name__} "
            f"(ID: {new_pipeline.pipeline_id})"
        )

    def process_data(self, data: str, type_data: str) -> str:
        if type_data == "JSON":
            for pipeline in self.pipelines:
                if isinstance(pipeline, JSONAdapter):
                    output = pipeline.process(data)
                    return output
            raise TypeError("No processing pipeline for json data")

        elif type_data == "CSV":
            for pipeline in self.pipelines:
                if isinstance(pipeline, CSVAdapter):
                    output = pipeline.process(data)
                    return output
            raise TypeError("No processing pipeline for csv data")

        elif type_data == "STREAM":
            for pipeline in self.pipelines:
                if isinstance(pipeline, StreamAdapter):
                    output = pipeline.process(data)
                    return output
            raise TypeError("No processing pipeline for stream data")

        return "the type of data is unkown and it can not be processed"


def main() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")

    manager = NexusManager()

    json_pipeline = JSONAdapter("JSON-001")
    json_pipeline.add_stage(InputStage())
    json_pipeline.add_stage(TransformStage())
    json_pipeline.add_stage(OutputStage())

    manager.add_pipeline(json_pipeline)

    csv_pipeline = CSVAdapter("CSV-001")
    csv_pipeline.add_stage(InputStage())
    csv_pipeline.add_stage(TransformStage())
    csv_pipeline.add_stage(OutputStage())

    manager.add_pipeline(csv_pipeline)

    stream_pipeline = StreamAdapter("STREAM-001")
    stream_pipeline.add_stage(InputStage())
    stream_pipeline.add_stage(TransformStage())
    stream_pipeline.add_stage(OutputStage())

    manager.add_pipeline(stream_pipeline)

    print("\n=== Multi-Format Data Processing ===\n")

    data = {"sensor": "temp", "value": 23.5, "unit": "C"}
    manager.process_data(data, "JSON")

    csv_data = "user,action,timestamp"
    manager.process_data(csv_data, "CSV")

    stream_data = "Real-time sensor stream"
    manager.process_data(stream_data, "STREAM")


if __name__ == "__main__":
    main()
