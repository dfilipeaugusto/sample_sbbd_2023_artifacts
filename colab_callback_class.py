import requests

class Integraviz(keras.callbacks.Callback):
    def __init__(self):
        self.unique_id = str(uuid.uuid4())

    def on_epoch_begin(self, epoch, logs=None):
        self.send_event('on_epoch_begin', datetime.now(), logs, epoch)

    def on_epoch_end(self, epoch, logs=None):
        self.send_event('on_epoch_end', datetime.now(), logs, epoch)

    def on_train_begin(self, logs=None):
        self.training_start = datetime.now()
        print(f"Starting training at {self.training_start}. ")
        self.send_event('on_train_begin', self.training_start, logs)

    def on_train_end(self, logs=None):
        self.training_end = datetime.now()
        print(f"Ending training at {self.training_end}. ")
        self.send_event('on_train_end', self.training_end, logs)


    def send_event(self, description, created_at, logs=None, epoch=None):
        tmp = {
            'id': self.unique_id,
            'description': description,
            'created_at': str(created_at)
          }

        if logs:
          tmp['logs'] = logs

        if epoch:
          tmp['epoch'] = epoch

        r = requests.post(
          'https://xpto_url.us-east-1.amazonaws.com/default/integraviz-rpc-xpto',
          headers={"Content-Type": "application/json"},
          json=tmp
        )

        print(r.status_code)

integraviz = Integraviz()
model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1, callbacks=[integraviz])
