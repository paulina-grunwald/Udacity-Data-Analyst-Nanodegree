// header
    var Title = d3.select('#title')
                                .append("h2")
                                .attr("width",590)
                                .attr("height",400)
                                .text("Survival Chance on the Titanic's passange");
//description 
    var Header = d3.select('#description')
                                .append("h3")
                                .text("CRMS titanic was a British passenger liner that sank in the North Atlantic Ocean in the early morning of 15 April 1912, after colliding with an iceberg during her maiden voyage from Southampton to New York City. Of the 2,224 passengers and crew aboard, more than 1,500 died in the sinking.")
                                .attr("align","center");
                                
// 1 - Titanic survivors based on class
    var width = 590,
        height = 400;
    var svg1 = dimple.newSvg("#chart1", width, height);
    d3.csv("titanic.csv", function(data){
        var chart = new dimple.chart(svg1, data);
        chart.addCategoryAxis("x", ["Class","Sex"]);
        chart.addMeasureAxis("y", "Survived");
        chart.addSeries("Sex", dimple.plot.bar);
        svg1.append("text")
         .attr("x", chart._xPixels() + chart._widthPixels() / 2)
         .attr("y", chart._yPixels() - 20)
         .style("text-anchor", "middle")
         .style("font-weight", "bold")
         .text("Survival Rate per class ");
    chart.addLegend(65, 10, 510, 20, "right");
    chart.draw();
    });

    // 2 - Titanic survivors based on age group
    var width = 590,
        height = 400;
    var svg2 = dimple.newSvg("#chart2", width, height);
    d3.csv("data/survival_age_group.csv", function(data){
        var chart = new dimple.chart(svg2, data);
        x = chart.addCategoryAxis("x", "Age Group");
        x.addOrderRule(["N/A", "0-15", "15-30", "30-45", "45-60", "60+"]);
        chart.addMeasureAxis("y", "Survival Rate");
        chart.addSeries(null,dimple.plot.bar);
        svg2.append("text")
         .attr("x", chart._xPixels() + chart._widthPixels() / 2)
         .attr("y", chart._yPixels() - 20)
         .style("text-anchor", "middle")
         .style("font-weight", "bold")
         .text("Survival Rate per age group");
    chart.draw();
    }); 

    // 3 - Titanic survivors based on parents/children 
    var width = 590,
        height = 400;
    var svg3 = dimple.newSvg("#chart3", width, height);
    d3.csv("data/survival_parc.csv", function(data){
        var chart = new dimple.chart(svg3, data);
        x = chart.addCategoryAxis("x", "Parch");
        chart.addMeasureAxis("y", "Survival Rate");
        chart.addSeries(null, dimple.plot.bar);
        svg3.append("text")
         .attr("x", chart._xPixels() + chart._widthPixels() / 2)
         .attr("y", chart._yPixels() - 20)
         .style("text-anchor", "middle")
         .style("font-weight", "bold")
         .text("Survival Rate split by parents with children");
      chart.draw();
      x.titleShape.text("Parents with children");
    });    