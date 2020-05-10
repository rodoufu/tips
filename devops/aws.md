# aws

## aws cli auto complete

```sh
complete -C '/usr/local/bin/aws_completer' aws
```

## Get Id and Key name of all intances running in ec2

```sh
aws ec2 describe-instances | jq '.Reservations | .[].Instances | .[].InstanceId,.[].KeyName'
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[KeyName,InstanceId, Placement.AvailabilityZone, State.Name]' --output text
```

```sh
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[KeyName,InstanceId, Placement.AvailabilityZone, State.Name,PrivateDnsNameq]' --output table
```

```sh
aws ec2 describe-key-pairs --query 'KeyPairs[*].KeyName'
```

## Get the log for a specific instance

```sh
aws ec2 get-console-output --instance-id i-0ba29afc833a46787 --latest | jq .Output
```

https://docs.aws.amazon.com/cli/latest/reference/ec2/get-console-output.html
