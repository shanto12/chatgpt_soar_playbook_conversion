"""
playbook 2 description
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'fl_filter_block_2' block
    fl_filter_block_2(container=container)

    return

"""
adfasdf
"""
def fl_filter_block_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('fl_filter_block_2() called')

    # collect filtered artifact ids for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["artifact:*.cef.bytesOut", "!=", ""],
        ],
        name="fl_filter_block_2:condition_1")

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        fb_get_something_2(action=action, success=success, container=container, results=results, handle=handle, custom_function=custom_function, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return

"""
hnmmm
"""
def fb_get_something_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('fb_get_something_2() called')
    
    template = """/playbooks/{0}"""

    # parameter list for template variable replacement
    parameters = [
        "filtered-data:fl_filter_block_2:condition_1:artifact:*.cef.bytesOut",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="fb_get_something_2", separator=", ")

    getting_some_data_2(container=container)

    return

"""
some desc here also hello.
"""
def getting_some_data_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('getting_some_data_2() called')

    # collect data for 'getting_some_data_2' call
    formatted_data_1 = phantom.get_format_data(name='fb_get_something_2')

    parameters = []
    
    # build parameters list for 'getting_some_data_2' call
    parameters.append({
        'location': formatted_data_1,
        'verify_certificate': False,
        'headers': "",
    })

    phantom.act(action="get data", parameters=parameters, assets=['http'], name="getting_some_data_2")

    return

def on_finish(container, summary):
    phantom.debug('on_finish() called')
    # This function is called after all actions are completed.
    # summary of all the action and/or all details of actions
    # can be collected here.

    # summary_json = phantom.get_summary()
    # if 'result' in summary_json:
        # for action_result in summary_json['result']:
            # if 'action_run_id' in action_result:
                # action_results = phantom.get_action_results(action_run_id=action_result['action_run_id'], result_data=False, flatten=False)
                # phantom.debug(action_results)

    return