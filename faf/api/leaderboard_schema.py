from marshmallow_jsonapi import Schema, fields


class LeaderboardSchema(Schema):
    """
    Represents ranked1v1 metadata
    """
    id = fields.String()
    login = fields.String()
    mean = fields.Float()
    deviation = fields.Float()
    num_games = fields.Integer()
    won_games = fields.Integer()
    lost_games = fields.Integer()
    winning_percentage = fields.Float()
    rating = fields.Integer()
    ranking = fields.Integer()

    class Meta:
        type_ = 'leaderboard'
