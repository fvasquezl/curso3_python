```
docker-compose build
docler-compose up -d
docker-compose exec app-csv bash
```
## Image commands
```docker image```
#### Commands:
<pre>
-  build       Build an image from a Dockerfile
-  history     Show the history of an image
-  import      Import the contents from a tarball to create a filesystem image
-  inspect     Display detailed information on one or more images
-  load        Load an image from a tar archive or STDIN
-  ls          List images
-  prune       Remove unused images
-  pull        Download an image from a registry
-  push        Upload an image to a registry
-  rm          Remove one or more images
-  save        Save one or more images to a tar archive (streamed to STDOUT by default)
-  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
</pre>
## Container commands
```docker container```
#### Commands:
<pre>
-  attach      Attach local standard input, output, and error streams to a running container
-  commit      Create a new image from a container's changes
-  cp          Copy files/folders between a container and the local filesystem
-  create      Create a new container
-  diff        Inspect changes to files or directories on a container's filesystem
-  exec        Execute a command in a running container
-  export      Export a container's filesystem as a tar archive
-  inspect     Display detailed information on one or more containers
-  kill        Kill one or more running containers
-  logs        Fetch the logs of a container
-  ls          List containers
-  pause       Pause all processes within one or more containers
-  port        List port mappings or a specific mapping for the container
-  prune       Remove all stopped containers
-  rename      Rename a container
-  restart     Restart one or more containers
-  rm          Remove one or more containers
-  run         Create and run a new container from an image
-  start       Start one or more stopped containers
-  stats       Display a live stream of container(s) resource usage statistics
-  stop        Stop one or more running containers
-  top         Display the running processes of a container
-  unpause     Unpause all processes within one or more containers
-  update      Update configuration of one or more containers
-  wait        Block until one or more containers stop, then print their exit codes
</pre>