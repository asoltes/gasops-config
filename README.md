# gas-config

Script Hierarchy

```
C:\USERS\ANDREW.SOLTES\ONEDRIVE - TRUSTWAVE HOLDINGS, INC\DOCUMENTS\GAS-CONFIG
├───scripts
│   ├───configs
│   │   └───__pycache__
│   ├───utils
│   │   └───__pycache__
│   └───__pycache__
└───templates
    └───es_migration

```

## Create Dev Console Template for ElasticSearch to Opensearch Migration

`python .\gasopsconfig.py -t es_migration --date 2021-11-30`

**Sample Output**

```bash
# get the snaphots for the specific date
GET _snapshot/siem/2021-11-30*

# check if the indicies for specific date is in the cluster
GET _cat/indices/siem_events_ng_0_day_2021_11_30

# restore the S3 snapshot to S3
POST _snapshot/siem/2021-11-30@CHANGE_ME_WITH_THE_SNAPSHOT_ID/_restore
{
   "indices":"siem_events_ng_*_day_2021_11_30",
   "index_settings":{
      "routing":{
         "allocation":{
            "require":{
               "tier":""
            }
         }
      }
   }
}

# get cluster status
GET /_cluster/health?pretty

# get the migration status
GET _ultrawarm/migration/_status?v

# get the diskUsedPercent and heapPercent via dev console
GET /_cat/nodes?v&h=name,role,master,load_1m,load_5m,load_15m,cpu,disk.total,disk.used,heapPercent,diskUsedPercent&s=diskUsedPercent:desc

# migrate the indices from hot to warm
POST _ultrawarm/migration/siem_events_ng_0_day_2021_11_30/_warm
POST _ultrawarm/migration/siem_events_ng_1_day_2021_11_30/_warm
POST _ultrawarm/migration/siem_events_ng_2_day_2021_11_30/_warm
POST _ultrawarm/migration/siem_events_ng_3_day_2021_11_30/_warm
POST _ultrawarm/migration/siem_events_ng_4_day_2021_11_30/_warm
POST _ultrawarm/migration/siem_events_ng_5_day_2021_11_30/_warm
POST _ultrawarm/migration/siem_events_ng_6_day_2021_11_30/_warm
POST _ultrawarm/migration/siem_events_ng_7_day_2021_11_30/_warm
POST _ultrawarm/migration/siem_events_ng_8_day_2021_11_30/_warm
POST _ultrawarm/migration/siem_events_ng_9_day_2021_11_30/_warm
POST _ultrawarm/migration/siem_events_ng_10_day_2021_11_30/_warm
POST _ultrawarm/migration/siem_events_ng_11_day_2021_11_30/_warm
POST _ultrawarm/migration/siem_events_ng_12_day_2021_11_30/_warm
POST _ultrawarm/migration/siem_events_ng_13_day_2021_11_30/_warm
POST _ultrawarm/migration/siem_events_ng_14_day_2021_11_30/_warm
POST _ultrawarm/migration/siem_events_ng_15_day_2021_11_30/_warm
POST _ultrawarm/migration/siem_events_ng_16_day_2021_11_30/_warm
POST _ultrawarm/migration/siem_events_ng_17_day_2021_11_30/_warm
POST _ultrawarm/migration/siem_events_ng_18_day_2021_11_30/_warm
POST _ultrawarm/migration/siem_events_ng_19_day_2021_11_30/_warm


# login to ansible to check the status of indices
curl -s "http://localhost:9200/_cat/indices?v&s=rep,index" | grep 2021_11_30

# login to ansible and login on sigproxy sshme emea sigproxy to check diskUsedPercent and heapPercent
curl -sXGET "http://localhost:9200/_cat/nodes?v&h=name,role,master,load_1m,load_5m,load_15m,cpu,disk.total,disk.used,diskUsedPercent,heapPercent&s=heapPercent:desc"

# for more info follow this wiki
https://wiki.trustwave.com/display/GAS/HOWTO+-+Restore+Elasticsearch+S3+snapshots+to+OpenSearch

```
