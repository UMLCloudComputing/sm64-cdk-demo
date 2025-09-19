import aws_cdk as core
import aws_cdk.assertions as assertions

from sm64_cdk_demo.sm64_cdk_demo_stack import Sm64CdkDemoStack

# example tests. To run these tests, uncomment this file along with the example
# resource in sm64_cdk_demo/sm64_cdk_demo_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Sm64CdkDemoStack(app, "sm64-cdk-demo")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
