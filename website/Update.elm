{-
   Excited without bugs, have fun ("▔□▔)/hi~♡ Nasy.
   -----------------------------------------------
   |
   |             *         *
   |                  .                .
   |           .
   |     *                      ,
   |                   .
   |
   |                               *
   |          |\___/|
   |          )    -(             .              '
   |         =\  -  /=
   |           )===(       *
   |          /   - \
   |          |-    |
   |         /   -   \     0.|.0
   |  NASY___\__( (__/_____(\=/)__+1s____________
   |  ______|____) )______|______|______|______|_
   |  ___|______( (____|______|______|______|____
   |  ______|____\_|______|______|______|______|_
   |  ___|______|______|______|______|______|____
   |  ______|______|______|______|______|______|_
   |  ___|______|______|______|______|______|____

   -----------------------------------------------

   Author              : Nasy https://nasy.moe <Nasy>
   Date                : Mar 10, 2018
   Email               : echo bmFzeXh4QGdtYWlsLmNvbQo= | base64 -D
   Filename            : update.elm
   Last modified by    : Nasy
   Last modified time  : Mar 10, 2018
   License             : MIT

   -----------------------------------------------

   There are more things in heaven and earth, Horatio, than are dreamt.
      From "Hamlet"
-}


module Update exposing (..)

import Commands exposing (fetch_blog, fetch_blogs)
import Models exposing (BlogModel, BlogsModel, Model, Route(..))
import Msgs exposing (Msg)
import Ports exposing (set_title, up2top, init_comment)
import RemoteData exposing (WebData)
import RouteUrl.Builder exposing (..)


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    let
        old_settings =
            model.settings

        new_setting title route =
            ( { old_settings | title = title, route = route }, title )
    in
        case msg of
            Msgs.OnFetchBlogs res ->
                case res of
                    RemoteData.Success _ ->
                        let
                            ( settings, title ) =
                                new_setting "Nasy Land" Normal
                        in
                            ( { model | blogs = res, settings = settings }
                            , set_title "Nasy Land"
                            )

                    other ->
                        let
                            ( settings, title ) =
                                new_setting "Nasy Land" NotFoundRoute
                        in
                            ( { model | blogs = res, settings = settings }
                            , set_title "Nasy Land"
                            )

            Msgs.OnFetchBlog res ->
                case res of
                    RemoteData.Success blog ->
                        let
                            ( settings, title ) =
                                new_setting blog.title BlogRoute
                        in
                            ( { model
                                | blog = res
                                , settings = settings
                              }
                            , set_title title
                            )

                    RemoteData.Failure err ->
                        let
                            ( settings, title ) =
                                new_setting "404 Not Found" NotFoundRoute
                        in
                            ( { model | settings = settings }, set_title title )

                    other ->
                        let
                            ( settings, title ) =
                                new_setting old_settings.title NotFoundRoute
                        in
                            ( { model | settings = settings }, Cmd.none )

            Msgs.OnLocationChange ->
                let
                    url =
                        model.settings.location.href

                    old_settings =
                        model.settings

                    settings route =
                        { old_settings | route = route }

                    new_model route =
                        { model | settings = settings route }
                in
                    case
                        path <| fromUrl url
                    of
                        [] ->
                            ( new_model Normal, fetch_blogs )

                        "blogs" :: r ->
                            ( new_model Normal, fetch_blogs )

                        "blog" :: blog_url ->
                            ( new_model BlogRoute
                            , String.join "/" blog_url |> fetch_blog
                            )

                        other ->
                            ( model, Cmd.none )

            Msgs.SetUrl url ->
                case
                    path <| fromUrl url
                of
                    [] ->
                        ( model, fetch_blogs )

                    "blogs" :: r ->
                        ( model, fetch_blogs )

                    "blog" :: blog_url ->
                        ( model
                        , String.join "blog_url" blog_url |> fetch_blog
                        )

                    other ->
                        ( model, Cmd.none )

            Msgs.ChangeNavF ->
                let
                    old_settings =
                        model.settings

                    old_nav =
                        old_settings.nav

                    navf =
                        case model.settings.nav.f of
                            True ->
                                False

                            False ->
                                True

                    settings =
                        { old_settings | nav = { old_nav | f = navf } }
                in
                    ( { model | settings = settings }, Cmd.none )

            Msgs.ChangeNavN ->
                let
                    old_settings =
                        model.settings

                    old_nav =
                        old_settings.nav

                    navn =
                        case model.settings.nav.n of
                            True ->
                                False

                            False ->
                                True

                    settings =
                        { old_settings | nav = { old_nav | n = navn } }
                in
                    ( { model | settings = settings }, Cmd.none )

            Msgs.Up2Top ->
                ( model, up2top "" )

            Msgs.InitComment ->
                ( model, init_comment "" )
