$('#date').on('click', function() {
    new Calendar({
        id: '#date',
        callback: function(y, m, d) {
            if (arguments.length > 1) {
                $('#date').html(y + '-' + m + '-' + d);
                $('.info').html('选定的时间是：' + y + '年' + m + '月' + d + '日');
            } else {
                $('.info').html('您为什么选择：' + y);
            }
 
        }
    })
})