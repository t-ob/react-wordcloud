var WordCloud = React.createClass({
  render: function() {
    var words = this.props.data.map(function (word) {
      return (
        <div>
          <h2>{word.text}</h2>
	  <p>{word.size}</p>
        </div>
      );
    });
    return (
      <div className="wordCloud">
        {words}
      </div>
    );
  }
});

var WordCloudBox = React.createClass({
  loadWordsFromServer: function() {
    $.ajax({
      url: this.props.url,
      dataType: 'json',
      cache: false,
      success: function(data) {
        this.setState({data: data});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },
  handleTwitterHandleSubmit: function(handle) {
    // todo
  },
  getInitialState: function() {
    return {data: []}
  },
  componentDidMount: function() {
    this.loadWordsFromServer();
  },
  render: function() {
    return (
      <div className="wordCloudBox">
        <h1>Word Cloud</h1>
        <WordCloud data={this.state.data} />
      </div>
    );
  }
});
