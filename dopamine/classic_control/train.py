


from absl import app
from absl import flags

from dopamine.classic_control import run_experiment
from dopamine.agents.a2c import a2c_agent

import tensorflow as tf


flags.DEFINE_string('agent_name', None, 'Name of the agent')
# flags.DEFINE_string('base_dir', None, 'Base directory to host all required sub-directories')
flags.DEFINE_string(
    'schedule', 'continuous_train',
    'The schedule with which to run the experiment and choose an appropriate '
    'Runner. Supported choices are '
    '{continuous_train, continuous_train_and_eval}.')

FLAGS = flags.FLAGS


def create_agent(sess, environment):
    return a2c_agent.A2CAgent(sess, environment.action_space.n)

def create_runner(create_agent_fn):
    return run_experiment.Runner(create_agent_fn)

def launch_experiment(create_runner_fn, create_agent_fn):
    runner = create_runner_fn(create_agent_fn)
    runner.run_experiment()

def main(unused_argv):
    tf.logging.set_verbosity(tf.logging.INFO)
    launch_experiment(create_runner, create_agent)

if __name__ == '__main__':
    app.run(main)