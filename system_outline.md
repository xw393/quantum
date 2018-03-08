Structure of the system  
```
quantum/  
    |_ Preprocessing  
        |_ calculate_return  
        |_ calculate_covariance  
    |_ strats  
        |_ strats_momentum  
        |_ strats_mvg_avg  
        |_ etc.  
    |_ metrics  
        |_ sharpe_ratio  
        |_ information_ratio  
        |_ max_drawdown  
    |_ implement  
```

work-flow: given a set of assets   
(1) processing data: get returns, fill missing values etc.   
(2) put the processed data into strategies, then get portfolio weight.   
(3) calculate portfolio returns based on the weights [1],  
    measure portfolio performances.  
    i) select best strategy (need a well-organized output)  
    ii) store the parameters of best strategy for later implementing  
** (4) implement strategies daily, if trading signals are triggered,  
       send alert to execute trades. [2]  

[1] each strategy will output a portfolio weight to construct the portfolio  
[2] data need to be kept updated.  
