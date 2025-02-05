# zond-genesis-generator

Create a zond consensus/execution layer testnet genesis and optionally expose it via a web server for testing purposes.

### Examples

Create a new file with your custom configuration in `./config/values.env`. You can use the [defaults.env](defaults/defaults.env) file as a template.

```sh
# Create the output directory
mkdir output

# Overwriting the config files and generating the EL and CL genesis
docker run --rm -it -u $UID -v $PWD/output:/data \
  -v $PWD/config/values.env:/config/values.env \
  theqrl/zond-genesis-generator:latest all

# Just creating the EL genesis
docker run --rm -it -u $UID -v $PWD/output:/data \
  -v $PWD/config/values.env:/config/values.env \
  theqrl/zond-genesis-generator:latest el

# Just creating the CL genesis
docker run --rm -it -u $UID -v $PWD/output:/data \
  -v $PWD/config/values.env:/config/values.env \
  theqrl/zond-genesis-generator:latest cl
```
### Environment variables

Name           | Default | Description
-------------- |-------- | ----
SERVER_ENABLED | false   | Enable a web server that will serve the generated files
SERVER_PORT    | 8000    | Web server port

Besides that, you can also use ENV vars in your configuration files. One way of doing this is via the [values.env](config-example/values.env) configuration file. These will be replaced during runtime.