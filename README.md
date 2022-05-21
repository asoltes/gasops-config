# gasops-templates

```
pip install -r .\requirements.txt
```

### Increase storm_num_task | long format | template
`python lazy_gasops.py --type change --mode increase -pe 11656 --prev 9 --desired 12 --region APJ --cg_range H --consumergroup Global_Correlation_Source_9`

### Decrease storm_num_task | short format | template
`python lazy_gasops.py -t change -m decrease  -r EMEA -pe 11656 -p 6 -d 3 -cgr I -cg Global_Correlation_Source_9`

### DECOM | template
`python lazy_gasops.py -type decomm -jid 1524`

### POST CHANGE | template
`python lazy_gasops.py -t post`

### CHECK CONSUMER LAG COMMAND
`python lazy_gasops.py -t alerts -cg Global_Correlation_Source_9 -r APJ`

### create POST hot to warm migration config
`python .\lazy_gasops.py -t es_migration --opensearch_date 2021-11-30`

```
usage: lazy_gasops.py [-h] [-m] [-cg] [-pe] [-p] [-d] [-r] [-cgr] [-jid] [-type]

Gasops Templates

options:
  -type , --type        input the task type eg: change|alerts|decomm
  -h, --help            show this help message and exit
  -m , --mode           input increase|decrease
  -cg , --consumergroup  consumer group eg: CDS_Event_Reader|Global_Correlation_Source_7
  -pe , --pe            input the red PE: 11656
  -p , --prev           input the current storm num task eg: 9
  -d , --desired        input the desired storm num task eg: 12
  -r , --region         input the region eg APJ|EMEA|AMS
  -cgr , --cg_range     input the letter of new service to be added
  -jid , --jira         input jira gasops ticket number
```