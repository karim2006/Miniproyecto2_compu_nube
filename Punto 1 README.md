# Miniproyecto2_compu_nube  

PUNTO 1:

C:\Users\joshe>kubectl get nodes
NAME                                    STATUS   ROLES   AGE    VERSION
aks-agentpool-12556306-vmss000000        Ready    <none>  41m    v1.29.8
aks-agentpool-12556306-vmss000001        Ready    <none>  41m    v1.29.8

C:\Users\joshe>kubectl get services
"kubectl" no se reconoce como un comando interno o externo,
programa o archivo por lotes ejecutable.

C:\Users\joshe>kubectl get service
"kubectl" no se reconoce como un comando interno o externo,
programa o archivo por lotes ejecutable.

C:\Users\joshe>kubectl get services
NAME              TYPE          CLUSTER-IP     EXTERNAL-IP     PORT(S)                     AGE
kubernetes        ClusterIP     10.0.0.1       <none>          443/TCP                     42m
order-service     ClusterIP     10.0.137.199   <none>          3000/TCP                    11m
product-service   ClusterIP     10.0.84.129    <none>          3002/TCP                    11m
rabbitmq          ClusterIP     10.0.206.154   <none>          5672/TCP, 15672/TCP         11m
store-front       LoadBalancer  10.0.255.1     4.200.58.127    80:30187/TCP                11m

C:\Users\joshe>kubectl get deployments
NAME              READY   UP-TO-DATE   AVAILABLE   AGE
order-service     1/1     1            1           11m
product-service   1/1     1            1           11m
rabbitmq          1/1     1            1           11m
store-front       1/1     1            1           11m
